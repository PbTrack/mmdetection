_base_ = './cascade_rcnn_r50_fpn_finetune_posetrack21.py'
model = dict(
    type='CascadeRCNN',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch',
        init_cfg=dict(
            type='Pretrained', checkpoint='open-mmlab://resnext101_64x4d')))

load_from = '/home/ucl/elen/bstandae/pb-track/weights/mmdetection/cascade_rcnn_x101_64x4d_fpn_1x_coco_20200515_075702-43ce6a30.pth'
