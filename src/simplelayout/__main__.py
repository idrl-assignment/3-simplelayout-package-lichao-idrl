# TODO 正确导入函数 generate_matrix, save_matrix, save_fig
from simplelayout.generator.utils import save_matrix, save_fig, make_dir
from simplelayout.generator.core import generate_matrix
from simplelayout.cli import get_options  # TODO: 保证不修改本行也可以正确导入


def main():
    options = get_options()
    board_grid = options.board_grid
    unit_grid = options.unit_grid
    unit_n = options.unit_n
    positions = options.positions
    file_name = options.file_name
    outdir = options.outdir
    nd_array = generate_matrix(board_grid, unit_grid, unit_n, positions)
    save_matrix(nd_array, file_name)
    save_fig(nd_array, file_name)
    make_dir(outdir)
      # TODO 使用导入的函数按命令行参数生成数据，包括 mat 文件与 jpg 文件


if __name__ == "__main__":
    main()
