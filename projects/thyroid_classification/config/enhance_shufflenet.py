_base_ = [
    r'D:\task\thyroid\ThyroidClassification\projects\thyroid_classification\_base_/enhance_shufflenet.py',  # 模型配置
    r'D:\task\thyroid\ThyroidClassification\projects\thyroid_classification\_base_/imagenet_bs64_pil_resize.py',  # 数据配置
    r'D:\task\thyroid\ThyroidClassification\projects\thyroid_classification\_base_/imagenet_bs1024_linearlr_bn_nowd.py',  # 训练策略配置
    r'D:\task\thyroid\ThyroidClassification\projects\thyroid_classification\_base_/default_runtime.py'  # 默认运行
]