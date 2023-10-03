from text_encoder import TextEncoder
from sentence_transformers import util
text_encoder = TextEncoder()

# 入力文をベクトル表現に変換
sentence = '今日は雨振らなくてよかった'
embedding = text_encoder.model.encode(sentence, convert_to_tensor=True)

# print(embedding)

# 検索対象文をベクトル表現に変換
sentences = [
    '好きな食べ物は何ですか?',
    'どこにお住まいですか?',
    '朝の電車は混みますね',
    '今日は良いお天気ですね',
    '最近景気悪いですね']
embeddings = text_encoder.model.encode(sentences, convert_to_tensor=True)

# 入力文と検索対象文のベクトル表現の類似度を計算
scores = util.pytorch_cos_sim(embedding, embeddings)
predicted_idx = scores.argmax(1).item() # スコアが最大のインデックスの取得
print('文:', sentence)
print('類似文:', sentences[predicted_idx])
print('類似度:', scores)

print(0)