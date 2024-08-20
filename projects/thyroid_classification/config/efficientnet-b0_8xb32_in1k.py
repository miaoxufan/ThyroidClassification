_base_ = [
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/efficientnet_b0.py',  # 模型配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs32.py',  # 数据配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/imagenet_bs256.py',  # 训练策略配置
    r'D:\task\thyroid\mmpretrain-main\projects\thyroid_classification\_base_/default_runtime.py'  # 默认
]

# dataset settings
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='EfficientNetRandomCrop', scale=224),
    dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    dict(type='PackInputs'),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='EfficientNetCenterCrop', crop_size=224),
    dict(type='PackInputs'),
]

train_dataloader = dict(dataset=dict(pipeline=train_pipeline))
val_dataloader = dict(dataset=dict(pipeline=test_pipeline))
test_dataloader = dict(dataset=dict(pipeline=test_pipeline))
