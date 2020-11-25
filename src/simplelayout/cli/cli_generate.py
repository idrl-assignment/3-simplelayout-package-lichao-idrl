import argparse


def get_options():
    parser = argparse.ArgumentParser()
    # TODO: 按 1-simplelayout-CLI 要求添加相应参数
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs='*',)
    parser.add_argument("--outdir", type=str, default="example_dir")
    parser.add_argument("--file_name", type=str, default="example")
    options = parser.parse_args()
    return options
