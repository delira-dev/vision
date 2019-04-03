
from delira import get_backends

if "TORCH" in get_backends():
    from .backends.resnet import ResNetTorch as ResNet, \
        BasicBlockTorch as BasicBlock, BottleneckTorch as Bottleneck
    from .backends.vgg import VGGTorch as VGG
    from .backends.alexnet import AlexNetTorch as AlexNet
    from .backends.squeezenet import SqueezeNetTorch
    from .backends.densenet import DenseNetTorch

    RESNET_CONFIGS = {
        '18': {"block": BasicBlock, "layers": [2, 2, 2, 2]},
        "34": {"block": BasicBlock, "layers": [3, 4, 6, 3]},
        "50": {"block": Bottleneck, "layers": [3, 4, 6, 3]},
        "101": {"block": Bottleneck, "layers": [3, 4, 23, 3]},
        "152": {"block": Bottleneck, "layers": [3, 8, 36, 3]},
    }

    VGG_CONFIGS = {
        '11': [64, 'P', 128, 'P', 256, 256, 'P', 512, 512, 'P', 512, 512, 'P'],
        '13': [64, 64, 'P', 128, 128, 'P', 256, 256, 'P', 512, 512, 'P', 512,
               512, 'P'],
        '16': [64, 64, 'P', 128, 128, 'P', 256, 256, 256, 'P', 512, 512, 512,
               'P', 512, 512, 512, 'P'],
        '19': [64, 64, 'P', 128, 128, 'P', 256, 256, 256, 256, 'P', 512, 512,
               512, 512, 'P', 512, 512, 512, 512, 'P'],
    }

    DENSENET_CONFIGS = {
        "121": {"num_init_features": 64, "growth_rate": 32,
                "block_config": (6, 12, 24, 16)},
        "161": {"num_init_features": 96, "growth_rate": 48,
                "block_config": (6, 12, 36, 24)},
        "169": {"num_init_features": 64, "growth_rate": 32,
                "block_config": (6, 12, 32, 32)},
        "201": {"num_init_features": 64, "growth_rate": 32,
                "block_config": (6, 12, 48, 32)},
    }

    def create_resnet_torch(num_layers: int, num_classes=1000, in_channels=3,
                            zero_init_residual=False, norm_layer=None, n_dim=2):
        config = RESNET_CONFIGS[str(num_layers)]

        return ResNet(config["block"], config["layers"],
                      num_classes=num_classes,
                      in_channels=in_channels,
                      zero_init_residual=zero_init_residual,
                      norm_layer=norm_layer, n_dim=n_dim)

    def create_vgg_torch(num_layers: int, num_classes=1000, in_channels=3,
                         init_weights=True, n_dim=2, norm_type="Batch",
                         pool_type="Max"):

        config = VGG_CONFIGS[str(num_layers)]

        return VGG(config, num_classes=num_classes,
                   in_channels=in_channels, init_weights=init_weights,
                   n_dim=n_dim, norm_type=norm_type, pool_type=pool_type)

    def create_densenet_torch(num_layers: int, bn_size=4, drop_rate=0,
                              num_classes=1000, n_dim=2, pool_type="Max",
                              norm_type="Batch"):
        config = DENSENET_CONFIGS[str(num_layers)]

        return DenseNetTorch(**config, bn_size=bn_size, drop_rate=drop_rate,
                             num_classes=num_classes, n_dim=n_dim,
                             pool_type=pool_type, norm_type=norm_type)

    def resnet18_torch(num_classes=1000, in_channels=3,
                       zero_init_residual=False, norm_layer=None, n_dim=2):
        """Constructs a ResNet-18 model.
        """
        return create_resnet_torch(18, num_classes=num_classes,
                                   in_channels=in_channels,
                                   zero_init_residual=zero_init_residual,
                                   norm_layer=norm_layer, n_dim=n_dim)

    def resnet34_torch(num_classes=1000, in_channels=3,
                       zero_init_residual=False, norm_layer=None, n_dim=2):
        """Constructs a ResNet-34 model.
        """
        return create_resnet_torch(34, num_classes=num_classes,
                                   in_channels=in_channels,
                                   zero_init_residual=zero_init_residual,
                                   norm_layer=norm_layer, n_dim=n_dim)


    def resnet50_torch(num_classes=1000, in_channels=3,
                       zero_init_residual=False, norm_layer=None, n_dim=2):
        """Constructs a ResNet-50 model.
        """
        return create_resnet_torch(50, num_classes=num_classes,
                                   in_channels=in_channels,
                                   zero_init_residual=zero_init_residual,
                                   norm_layer=norm_layer, n_dim=n_dim)


    def resnet101_torch(num_classes=1000, in_channels=3,
                        zero_init_residual=False, norm_layer=None, n_dim=2):
        """Constructs a ResNet-101 model.
        """
        return create_resnet_torch(101, num_classes=num_classes,
                                   in_channels=in_channels,
                                   zero_init_residual=zero_init_residual,
                                   norm_layer=norm_layer, n_dim=n_dim)

    def resnet152_torch(num_classes=1000, in_channels=3,
                        zero_init_residual=False, norm_layer=None, n_dim=2):
        """Constructs a ResNet-152 model.
        """
        return create_resnet_torch(152, num_classes=num_classes,
                                   in_channels=in_channels,
                                   zero_init_residual=zero_init_residual,
                                   norm_layer=norm_layer, n_dim=n_dim)


    def vgg11_torch(num_classes=1000, in_channels=3, init_weights=True, n_dim=2,
                    norm_type="Batch", pool_type="Max"):

        return create_vgg_torch(11, num_classes=num_classes,
                                in_channels=in_channels,
                                init_weights=init_weights, n_dim=n_dim,
                                norm_type=norm_type, pool_type=pool_type)

    def vgg13_torch(num_classes=1000, in_channels=3, init_weights=True, n_dim=2,
                    norm_type="Batch", pool_type="Max"):

        return create_vgg_torch(13, num_classes=num_classes,
                                in_channels=in_channels,
                                init_weights=init_weights, n_dim=n_dim,
                                norm_type=norm_type, pool_type=pool_type)

    def vgg16_torch(num_classes=1000, in_channels=3, init_weights=True, n_dim=2,
                    norm_type="Batch", pool_type="Max"):

        return create_vgg_torch(16, num_classes=num_classes,
                                in_channels=in_channels,
                                init_weights=init_weights, n_dim=n_dim,
                                norm_type=norm_type, pool_type=pool_type)

    def vgg19_torch(num_classes=1000, in_channels=3, init_weights=True, n_dim=2,
                    norm_type="Batch", pool_type="Max"):

        return create_vgg_torch(19, num_classes=num_classes,
                                in_channels=in_channels,
                                init_weights=init_weights, n_dim=n_dim,
                                norm_type=norm_type, pool_type=pool_type)

    def alexnet_torch(num_classes=1000, in_channels=3, n_dim=2,
                      pool_type="Max"):
        return AlexNet(num_classes=num_classes, in_channels=in_channels,
                       n_dim=n_dim, pool_type=pool_type)


    def squeezenet1_0_torch(num_classes=1000, n_dim=2,
                            pool_type="Max", p_dropout=0.5):
        r"""SqueezeNet model architecture from the `"SqueezeNet: AlexNet-level
        accuracy with 50x fewer parameters and <0.5MB model size"
        <https://arxiv.org/abs/1602.07360>`_ paper.
        """
        return SqueezeNetTorch(version=1.0, num_classes=num_classes,
                               n_dim=n_dim,
                               pool_type=pool_type, p_dropout=p_dropout)

    def squeezenet1_1_torch(num_classes=1000, n_dim=2,
                            pool_type="Max", p_dropout=0.5):
        r"""SqueezeNet 1.1 model from the `official SqueezeNet repo
        <https://github.com/DeepScale/SqueezeNet/tree/master/SqueezeNet_v1.1>`_.
        SqueezeNet 1.1 has 2.4x less computation and slightly fewer parameters
        than SqueezeNet 1.0, without sacrificing accuracy.
        """
        return SqueezeNetTorch(version=1.1, num_classes=num_classes,
                               n_dim=n_dim,
                               pool_type=pool_type, p_dropout=p_dropout)

    def densenet_121_torch(bn_size=4, drop_rate=0, num_classes=1000,
                           n_dim=2, pool_type="Max", norm_type="Batch"):
        return create_densenet_torch(121, bn_size=bn_size, drop_rate=drop_rate,
                                     num_classes=num_classes, n_dim=n_dim,
                                     pool_type=pool_type, norm_type=norm_type)

    def densenet_161_torch(bn_size=4, drop_rate=0, num_classes=1000,
                           n_dim=2, pool_type="Max", norm_type="Batch"):
        return create_densenet_torch(161, bn_size=bn_size, drop_rate=drop_rate,
                                     num_classes=num_classes, n_dim=n_dim,
                                     pool_type=pool_type, norm_type=norm_type)

    def densenet_169_torch(bn_size=4, drop_rate=0, num_classes=1000,
                           n_dim=2, pool_type="Max", norm_type="Batch"):
        return create_densenet_torch(169, bn_size=bn_size, drop_rate=drop_rate,
                                     num_classes=num_classes, n_dim=n_dim,
                                     pool_type=pool_type, norm_type=norm_type)

    def densenet_201_torch(bn_size=4, drop_rate=0, num_classes=1000,
                           n_dim=2, pool_type="Max", norm_type="Batch"):
        return create_densenet_torch(201, bn_size=bn_size, drop_rate=drop_rate,
                                     num_classes=num_classes, n_dim=n_dim,
                                     pool_type=pool_type, norm_type=norm_type)
