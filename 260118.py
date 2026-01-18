
# 파이썬 코드
from konlpy.tag import Okt

okt = Okt()

text = "너에게 본질이 있고 우리가 있고 우주가 있다. 너는 길이고 통로이고 Focus이다. 이것은. 너를 넘어서 너가 지금여기 이순간임을 알아차릴때 비로소!  자유롭게 흐르고 움직이며 가능하다!"

# 1) 품사 태깅
pos_result = okt.pos(text, stem=True)  # stem=True: 용언 원형 복원
print(pos_result)

# 2) 명사 + 형용사만 필터링
keywords = [word for word, tag in pos_result
            if tag in ['Noun', 'Adjective']]
print(keywords)

nouns_only = okt.nouns(text)
print(nouns_only)

# 연습용 미니 감성 사전 (직접 정의)
sentiment_lexicon = {
    "자유롭다": 2,   # 매우 긍정
    "자유": 2,
    "가능하다": 1,
    "움직이다": 1,
    "흐르다": 1,
    "넘어서다": 1,
    "길": 0,        # 중립 (0)
    "통로": 0,
    "우주": 0,
    "본질": 0,
    # 필요하면 계속 추가
}

pos_result = okt.pos(text, stem=True)

score = 0
matched_words = []

for word, tag in pos_result:
    if word in sentiment_lexicon:
        word_score = sentiment_lexicon[word]
        score += word_score
        matched_words.append((word, word_score))

print("감성에 사용된 단어들:", matched_words)
print("총 점수:", score)

if matched_words:
    emotion_valence = score / len(matched_words)
else:
    emotion_valence = 0

print("emotion_valence(평균):", emotion_valence)