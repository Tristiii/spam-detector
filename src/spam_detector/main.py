from predict import predict_text
from train import train_model

print('Hello! I am a spam detector.')
print(f'Accuracy: {round(train_model() * 100, 2)}%')

online = True
while online:
    i = input('Enter command: ')

    match i.split(maxsplit=1):
        case ['quit']:
            online = False
        case ['predict', text]:
            print(predict_text(text))
        case _:
            print('I do not recognize that command.')
