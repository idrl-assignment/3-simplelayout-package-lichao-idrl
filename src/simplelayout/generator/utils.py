"""
辅助函数
"""

from pathlib import Path
import matplotlib.pyplot as plt
import scipy.io as sio


def save_matrix(matrix, file_name):
    # TODO: 存储 matrix 到 file_name.mat, mdict 的 key 为 "matrix"
    file_name = file_name + '.mat'
    sio.savemat(file_name, mdict = {"matrix": matrix})



def save_fig(matrix, file_name):
    # TODO: 将 matrix 画图保存到 file_name.jpg
    plt.imshow(matrix)
    file_name = file_name + '.jpg'
    plt.savefig(file_name)



def make_dir(outdir):
    # TODO: 当目录 outdir 不存在时创建目录
    Path.mkdir(outdir)

