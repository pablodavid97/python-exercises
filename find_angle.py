from math import acos, sqrt, degrees, ceil

def find_angle(ab_side, bc_side):
    calculation = bc_side / sqrt(bc_side**2 + ab_side**2)
    mbc = degrees(acos(calculation))
    return ceil(round(mbc, 1))

def main():
    ab_input = int(input())
    bc_input = int(input())

    if ab_input <= 0 or ab_input > 100:
        print('Invalid input!')
        return
    elif bc_input <= 0 or bc_input > 100:
        print('Invalid input!')
        return
    
    print(find_angle(ab_input, bc_input))

if __name__ == '__main__':
    main()