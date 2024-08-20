_base_ = [
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/hrnet-w18.py',  # 模型配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs32_pil_resize.py',  # 数据配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs256_coslr.py',  # 训练策略配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/default_runtime.py'  # 默认
]

# NOTE: `auto_scale_lr` is for automatically scaling LR
# based on the actual training batch size.
# base_batch_size = (4 GPUs) x (32 samples per GPU)
auto_scale_lr = dict(base_batch_size=128)
