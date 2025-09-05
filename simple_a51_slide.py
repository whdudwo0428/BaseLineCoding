#!/usr/bin/env python3
"""
Simple A5/1 (slide spec) — single file

Spec (from slide):
- Registers: X(5), Y(6), Z(7)
- Feedback taps (LSB-indexed in the slide):
    X_fb = X4 ⊕ X2
    Y_fb = Y5 ⊕ Y1
    Z_fb = Z6 ⊕ Z5 ⊕ Z1
- Clock bits for majority clocking:
    clk(X)=X2, clk(Y)=Y3, clk(Z)=Z4
- Init: all zeros
- Load Kc (default 0xBEEF, 16 bits MSB→LSB), then FN (default 0x3A, 8 bits MSB→LSB)
  During loading, all three LFSRs shift each step with inj = fb XOR input_bit
- Warm-up: N cycles of majority clocking (default 10), inj = fb (no external bit)
- Keystream: M bits (default 8) using same majority rule;
  output bit per cycle = XOR of MSBs AFTER the clock (X5 ⊕ Y6 ⊕ Z7)

CLI:
    python simple_a51_slide.py
    python simple_a51_slide.py --kc BEEF --fn 3A --warmup 10 --ks 8
    python simple_a51_slide.py --csv steps.csv   # save all steps to CSV
    python simple_a51_slide.py --verbose         # print step log to stdout
"""
from __future__ import annotations
import argparse, csv
from typing import List, Tuple, Dict

# ---------- helpers ----------
def hex_to_bits(hex_str: str, bitlen: int) -> List[int]:
    """Return MSB→LSB bit list of given width from hex string (with/without 0x)."""
    v = int(hex_str, 16) if not hex_str.lower().startswith("0x") else int(hex_str, 16)
    return [(v >> (bitlen - 1 - i)) & 1 for i in range(bitlen)]

def shift_in(reg: List[int], inj: int) -> List[int]:
    """Left shift (drop MSB), append inj at LSB."""
    return reg[1:] + [inj]

def majority(a: int, b: int, c: int) -> int:
    return (a & b) | (a & c) | (b & c)

def bits_to_str(reg: List[int]) -> str:
    return ''.join(str(b) for b in reg)

# Feedback taps (arrays are MSB..LSB: X=[X5,X4,X3,X2,X1])
def fb_X(X: List[int]) -> int: return X[1] ^ X[3]           # X4 ^ X2
def fb_Y(Y: List[int]) -> int: return Y[1] ^ Y[5]           # Y5 ^ Y1
def fb_Z(Z: List[int]) -> int: return Z[1] ^ Z[2] ^ Z[6]    # Z6 ^ Z5 ^ Z1

# Clock bits (LSB-indexed in slide): X2, Y3, Z4
def clk_X(X: List[int]) -> int: return X[-2]
def clk_Y(Y: List[int]) -> int: return Y[-3]
def clk_Z(Z: List[int]) -> int: return Z[-4]

# ---------- core ----------
def simple_a51(kc_hex: str="BEEF", fn_hex: str="3A", warmup: int=10, ks_bits: int=8,
               verbose: bool=False) -> Tuple[List[int], List[Dict[str, object]]]:
    # Registers (MSB..LSB)
    X = [0]*5; Y = [0]*6; Z = [0]*7
    steps: List[Dict[str, object]] = []

    def add_row(stage, step, in_src, in_bit, Xv, Yv, Zv, FX, FY, FZ, cx, cy, cz, maj, injx, injy, injz, NX, NY, NZ, out="-"):
        row = {
            "STAGE": stage, "STEP": step, "IN_SRC": in_src, "IN_BIT": in_bit,
            "X": bits_to_str(Xv), "Y": bits_to_str(Yv), "Z": bits_to_str(Zv),
            "fbX": FX, "fbY": FY, "fbZ": FZ,
            "CLKs(X2/Y3/Z4)": f"{cx}/{cy}/{cz}", "MAJ": maj,
            "injX": injx, "injY": injy, "injZ": injz,
            "NX": bits_to_str(NX), "NY": bits_to_str(NY), "NZ": bits_to_str(NZ),
            "OUT": out
        }
        steps.append(row)
        if verbose:
            print(row)

    # 0) initial
    add_row("init", 0, "-", "-", X, Y, Z, "-", "-", "-", "-", "-", "-", "-", "-", "-", X, Y, Z, "-")

    # 1) Load Kc (16 bits, MSB→LSB)
    Kc_bits = hex_to_bits(kc_hex, 16)
    for i,b in enumerate(Kc_bits, 1):
        FX,FY,FZ = fb_X(X), fb_Y(Y), fb_Z(Z)
        injx,injy,injz = FX ^ b, FY ^ b, FZ ^ b
        Xn,Yn,Zn = shift_in(X,injx), shift_in(Y,injy), shift_in(Z,injz)
        add_row("load_Kc", i, "Kc", b, X,Y,Z, FX,FY,FZ, clk_X(X),clk_Y(Y),clk_Z(Z), "-", injx,injy,injz, Xn,Yn,Zn, "-")
        X,Y,Z = Xn,Yn,Zn

    # 2) Load FN (8 bits, MSB→LSB)
    FN_bits = hex_to_bits(fn_hex, 8)
    for j,b in enumerate(FN_bits, 1):
        FX,FY,FZ = fb_X(X), fb_Y(Y), fb_Z(Z)
        injx,injy,injz = FX ^ b, FY ^ b, FZ ^ b
        Xn,Yn,Zn = shift_in(X,injx), shift_in(Y,injy), shift_in(Z,injz)
        add_row("load_FN", j, "FN", b, X,Y,Z, FX,FY,FZ, clk_X(X),clk_Y(Y),clk_Z(Z), "-", injx,injy,injz, Xn,Yn,Zn, "-")
        X,Y,Z = Xn,Yn,Zn

    # 3) Warm-up (majority clocking)
    for w in range(1, warmup+1):
        cx,cy,cz = clk_X(X), clk_Y(Y), clk_Z(Z)
        m = majority(cx,cy,cz)
        FX,FY,FZ = fb_X(X), fb_Y(Y), fb_Z(Z)
        Xn,Yn,Zn = X[:],Y[:],Z[:]
        injx=injy=injz="-"
        if cx==m: Xn = shift_in(X,FX); injx=FX
        if cy==m: Yn = shift_in(Y,FY); injy=FY
        if cz==m: Zn = shift_in(Z,FZ); injz=FZ
        add_row("warmup", w, "-", "-", X,Y,Z, FX,FY,FZ, cx,cy,cz, m, injx,injy,injz, Xn,Yn,Zn, "-")
        X,Y,Z = Xn,Yn,Zn

    # 4) Keystream generation
    out_bits: List[int] = []
    for k in range(1, ks_bits+1):
        cx,cy,cz = clk_X(X), clk_Y(Y), clk_Z(Z)
        m = majority(cx,cy,cz)
        FX,FY,FZ = fb_X(X), fb_Y(Y), fb_Z(Z)
        Xn,Yn,Zn = X[:],Y[:],Z[:]
        injx=injy=injz="-"
        if cx==m: Xn = shift_in(X,FX); injx=FX
        if cy==m: Yn = shift_in(Y,FY); injy=FY
        if cz==m: Zn = shift_in(Z,FZ); injz=FZ
        out = Xn[0] ^ Yn[0] ^ Zn[0]  # XOR of MSBs after clock
        out_bits.append(out)
        add_row("keystream", k, "-", "-", X,Y,Z, FX,FY,FZ, cx,cy,cz, m, injx,injy,injz, Xn,Yn,Zn, out)
        X,Y,Z = Xn,Yn,Zn

    return out_bits, steps

def write_csv(steps: List[dict], path: str):
    if not steps: return
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(steps[0].keys()))
        w.writeheader()
        for r in steps:
            w.writerow(r)

def main():
    ap = argparse.ArgumentParser(description="Simple A5/1 (slide spec)")
    ap.add_argument("--kc", default="BEEF", help="Kc hex (default: BEEF)")
    ap.add_argument("--fn", default="3A", help="FN hex (default: 3A)")
    ap.add_argument("--warmup", type=int, default=10, help="Warm-up cycles (default: 10)")
    ap.add_argument("--ks", type=int, default=8, help="Keystream bits to output (default: 8)")
    ap.add_argument("--csv", default="", help="Optional CSV path to save full step log")
    ap.add_argument("--verbose", action="store_true", help="Print step rows to stdout")
    args = ap.parse_args()

    out, steps = simple_a51(args.kc, args.fn, args.warmup, args.ks, verbose=args.verbose)
    print("Keystream bits:", out)
    print("Keystream as string:", ''.join(str(b) for b in out))
    if args.csv:
        write_csv(steps, args.csv)
        print(f"Wrote step log to: {args.csv}")

if __name__ == "__main__":
    main()
