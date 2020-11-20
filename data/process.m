cfg = [];
cfg.method = 'degrees';
cfg.parameter = 'cohspctrm';
cfg.threshold = .1;

network = ft_networkanalysis(cfg, connEEGbroad);

cfg = [];
cfg.method = 'surface';
cfg.funparameter = 'degrees';
cfg.funcolormap = 'jet';
ft_soruceplot(cfg, network)
view([-150 30])







