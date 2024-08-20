_base_ = [
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/shufflenet_v2_1x.py',  # 模型配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs64_pil_resize.py',  # 数据配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs1024_linearlr_bn_nowd.py',  # 训练策略配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/default_runtime.py'  # 默认运行
]
