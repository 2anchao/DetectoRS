_base_ = '../htc/htc_r50_fpn_1x_coco.py'

model = dict(
    backbone=dict(conv_cfg=dict(type="ConvAWS"), output_img=True),
    neck=dict(
        type='RFP',
        rfp_steps=2,
        rfp_backbone=dict(
            rfp_inp=256,
            type='ResNet',
            depth=50,
            num_stages=4,
            out_indices=(0, 1, 2, 3),
            frozen_stages=1,
            norm_cfg=dict(type='BN', requires_grad=True),
            norm_eval=True,
            conv_cfg=dict(type='ConvAWS'),
            style='pytorch'),
        rfp_pretrained='torchvision://resnet50',
    )
)
