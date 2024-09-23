from argparse import ArgumentParser
from mmengine.fileio import dump
from rich import print_json
from mmpretrain.apis import ImageClassificationInferencer
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
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

    y_true = []
    y_scores = []

    for dirpath, dirs, files in os.walk(args.dir):

        for file in files:
            first_char = file[0]
            test_file = dirpath + '/' + file
            result = inferencer(test_file, show=args.show, show_dir=args.show_dir)[0]
            #result.pop('pred_scores')  # pred_scores is too verbose for a demo.
            print_json(dump(result, file_format='json', indent=4))

            # true_label = result.get('pred_label')  # Adjust if needed
            if first_char == "B":
                true_label = 0
            else:
                true_label = 1
            pred_scores = result.get('pred_score')  # Adjust if needed

            if true_label is not None and pred_scores is not None:
                y_true.append(true_label)
                y_scores.append(pred_scores)

    # y_true = [item for sublist in y_true for item in sublist]
    # y_scores = [item for sublist in y_scores for item in sublist]

    print(f"y_true: {y_true}")  # Debug line
    print(f"y_scores: {y_scores}")  # Debug line

    if not y_true or not y_scores:
        print("Error: No data available for AUC calculation.")
        return

    # Compute AUC
    # y_true = [0] * 82 + [1] * 124
    # for index, value in enumerate(y_true):
    #     if value == 1:
    #         temp = y_scores[index]
    #         y_scores[index] = 1 - temp
    # print(y_scores)

    # print(y_true)
    auc = roc_auc_score(y_true, y_scores)
    print(f"AUC: {auc}")

if __name__ == '__main__':
    main()

