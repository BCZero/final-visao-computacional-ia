from ultralytics import YOLO

path_config_yaml = 'config.yaml'
projeto = "transfer_v1_ep30"
nome_modelo = "yolo_transfer"

# Caminho corrigido com o prefixo 'runs/detect/'
best_model_path = f'runs/detect/{projeto}/{nome_modelo}/weights/best.pt'

# Carrega o modelo que você acabou de treinar
yolo_best = YOLO(best_model_path)

def print_metricas(model, particao):
    if particao not in ('val', 'test'):
        print('particao invalida')
        return
    
    # Extrai as métricas
    metricas = model.val(data=path_config_yaml, verbose=False, split=particao)
    
    print('\n\n' + 30*'-')
    print(f'Métricas partição: {particao.upper()}')
    print(30*'-')
    print(f'   mAP@0.50          : {metricas.box.map50:0.3f}')
    print(f'   mAP@0.50:0.95     : {metricas.box.map:0.3f}')
    print(f'   Precisao media    : {metricas.box.mp:0.3f}')
    print(f'   Recall medio      : {metricas.box.mr:0.3f}')
    print(60*'-')
    
    for i, cls_idx in enumerate(metricas.box.ap_class_index):
        nome = model.names[cls_idx]
        ap = metricas.box.ap50[i]
        print(f'   {int(cls_idx)} {nome:<15} AP@50 = {ap:.4f}')

# Exibe os resultados na tela
print_metricas(yolo_best, 'val')