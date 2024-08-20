from argparse import ArgumentParser
from mmengine.fileio import dump
from rich import print_json
from mmpretrain.apis import ImageClassificationInferencer
import matplotlib.pyplot as plt
import os

def main():
    parser = ArgumentParser()
    parser.add_argument('img', help='Image file')
    parser.add_argument('model', help='Model name or config file path')
    parser.add_argument('--dir', help='Test direction')
    parser.add_argument('--checkpoint', help='Checkpoint file path.')
    parser.add_argument(
        '--show',
        action='store_true',
        help='Whether to show the prediction result in a window.')
    parser.add_argument(
        '--show-dir',
        type=str,
        help='The directory to save the visualization image.')
    parser.add_argument('--device', help='Device used for inference')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    try:
        pretrained = args.checkpoint or True
        inferencer = ImageClassificationInferencer(
            args.model, pretrained=pretrained)
    except ValueError:
        raise ValueError(
            f'Unavailable model "{args.model}", you can specify find a model '
            'name or a config file or find a model name from '
            'https://mmpretrain.readthedocs.io/en/latest/modelzoo_statistics.html#all-checkpoints'  # noqa: E501
        )

    for dirpath, dirs, files in os.walk(args.dir):
        benign = 0
        malignant = 0
        for file in files:
            test_file = dirpath + '/' + file
            result = inferencer(test_file, show=args.show, show_dir=args.show_dir)[0]
            # result.pop('pred_scores')  # pred_scores is too verbose for a demo.
            print_json(dump(result, file_format='json', indent=4))
            diagnosis = result.get('pred_class')
            if diagnosis == "Benign":
                benign += 1
            else:
                malignant += 1
            # print_json(dump(result, file_format='json', indent=4))
    print('---------------')
    print('良性图片数为',benign)
    print('恶性图片数为',malignant)

    # result = inferencer(args.img, show=args.show, show_dir=args.show_dir)[0]
    # # show the results
    # result.pop('pred_scores')  # pred_scores is too verbose for a demo.
    # print_json(dump(result, file_format='json', indent=4))

if __name__ == '__main__':
    main()
