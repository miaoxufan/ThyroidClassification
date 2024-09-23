# model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(type='Enhance_ShuffleNet', widen_factor=1.0),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=2,
        in_channels=1024,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, ),
    ))