_base_ = [
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/res2net50-w14-s8.py',#模型配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs32_pil_resize.py',#数据配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs256.py',#训练策略配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/default_runtime.py'#默认运行设置
]