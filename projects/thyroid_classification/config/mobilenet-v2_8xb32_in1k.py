_base_ = [
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/mobilenet_v2_1x.py',#模型配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs32_pil_resize.py',#数据配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs256_epochstep.py',#训练策略配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/default_runtime.py'#默认运行
]
