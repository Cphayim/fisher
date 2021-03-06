# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/6/27 15:41
"""

__author__ = 'Cphayim'

# 资源是稀缺的
# 计算机资源 竞争计算机的资源
# 进程
# 一个应用程序至少有一个进程
# 进程是竞争计算机资源的基本单位

# 单个 CPU 核心 同一时刻只能有一个进程使用 CPU 资源
# 在不同的应用程序进程之间切换
# 进程调度（操作系统最核心的功能）算法 （决定什么时候将一个进程挂起切换到另外一个进程）
# 进程/线程切换 对系统的开销非常大 （因为上下文切换需要保存程序当前的状态）

# 线程 线程是进程的一部分 1个进程 多个线程
# 线程产生的原因是因为现代的 CPU 运行越来越快，
# 如果只是用进程来管理 CPU 资源，粒度太大了，不能够有效和充分的利用 CPU 的高性能
# 需要一个更小的单元来协调 CPU 资源利用
# 线程比进程更加灵活小巧，线程切换消耗的资源远比进程切换消耗要来的小

# 进程和线程的分工不同
# 进程用来分配资源，比如内存资源
# 线程是用来利用 CPU 执行代码

# 线程也可以访问资源
# 线程是属于一个进程的，线程自己不拥有资源，但是可以访问它所在的进程的资源