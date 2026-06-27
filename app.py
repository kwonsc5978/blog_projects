from flask import Flask, render_template, abort

app = Flask(__name__)

POSTS = [
    {
        "id": 1,
        "title": "봄날의 산책",
        "category": "일상",
        "date": "2026.06.01",
        "author": "Annabelle",
        "image": "https://images.unsplash.com/photo-1522383225653-ed111181a951?auto=format&fit=crop&w=900&q=80",
        "summary": "따뜻한 햇살과 함께한 오랜만의 산책 이야기입니다.",
        "content": """
오늘은 날씨가 정말 좋아서 가까운 공원으로 산책을 다녀왔어요.
연한 분홍빛 꽃들이 피어 있어서 마음까지 부드러워지는 하루였습니다.

가끔은 멀리 여행을 가지 않아도, 집 근처에서 충분히 좋은 시간을 보낼 수 있는 것 같아요.
"""
    },
    {
        "id": 2,
        "title": "나만의 홈카페 만들기",
        "category": "라이프",
        "date": "2026.06.05",
        "author": "Annabelle",
        "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=900&q=80",
        "summary": "집에서도 분위기 있는 카페를 만드는 작은 방법들.",
        "content": """
커피 한 잔과 조용한 음악만 있어도 집이 작은 카페처럼 느껴질 때가 있어요.

오늘은 좋아하는 컵, 따뜻한 조명, 작은 식물 하나로 홈카페 분위기를 만들어봤습니다.
"""
    },
    {
        "id": 3,
        "title": "제주도 여행 기록 #2",
        "category": "여행",
        "date": "2026.06.10",
        "author": "Annabelle",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80",
        "summary": "파란 바다와 조용한 카페가 좋았던 제주 여행.",
        "content": """
제주도의 바다는 언제 봐도 좋습니다.

이번 여행에서는 유명한 관광지보다 조용한 해변과 작은 카페를 중심으로 다녔어요.
천천히 걷고, 바람을 느끼는 시간이 참 좋았습니다.
"""
    },
    {
        "id": 4,
        "title": "좋아하는 음악 기록",
        "category": "음악",
        "date": "2026.06.15",
        "author": "Annabelle",
        "image": "https://images.unsplash.com/photo-1511379938547-c1f69419868d?auto=format&fit=crop&w=900&q=80",
        "summary": "요즘 자주 듣는 노래와 플레이리스트 소개.",
        "content": """
요즘은 잔잔한 어쿠스틱 음악을 자주 듣고 있어요.

일을 하거나 글을 쓸 때 너무 시끄럽지 않은 음악이 집중에 도움이 됩니다.
"""
    },
]

CATEGORIES = ["일상", "라이프", "여행", "음악", "생각"]


@app.route("/")
def index():
    return render_template("index.html", posts=POSTS, categories=CATEGORIES)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = next((p for p in POSTS if p["id"] == post_id), None)

    if post is None:
        abort(404)

    return render_template("post_detail.html", post=post)


@app.route("/category/<category_name>")
def category(category_name):
    filtered_posts = [p for p in POSTS if p["category"] == category_name]

    return render_template(
        "category.html",
        category_name=category_name,
        posts=filtered_posts,
        categories=CATEGORIES
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
