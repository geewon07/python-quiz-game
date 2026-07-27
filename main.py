"""나만의 퀴즈 게임 - 콘솔 애플리케이션"""

MENU = """
========================================
        🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================"""

class Quiz:
    """개별 퀴즈 한 문제를 표현하는 클래스"""

    def __init__(self, question, choices, answer):  #생성자
        self.question = question    # 문제 (str)
        self.choices = choices      # 선택지 4개 (list)
        self.answer = answer        # 정답 번호 1~4 (int)

    def show(self, number=None):
        """문제와 선택지를 화면에 출력한다."""
        title = f"[문제 {number}]" if number else "[문제]"
        print(f"\n{title}")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 입력한 번호가 정답인지 판별한다."""
        return user_answer == self.answer

    def answer_text(self):
        """정답 선택지의 실제 내용을 반환한다."""
        return self.choices[self.answer - 1]

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리(JSON에서 읽은 데이터)로부터 Quiz 객체를 생성한다."""
        return cls(data["question"], data["choices"], data["answer"])

DEFAULT_QUIZ_DATA = [
    {
        "question": "range(1, 10, 2)가 만들어내는 숫자의 개수는?",
        "choices": ["4개", "5개", "9개", "10개"],
        "answer": 2,
    },
    {
        "question": "다음 중 생성 후 값을 변경할 수 없는(불변) 자료형은?",
        "choices": ["list", "dict", "tuple", "set"],
        "answer": 3,
    },
    {
        "question": "딕셔너리에 존재하지 않는 키로 접근하면 발생하는 예외는?",
        "choices": ["IndexError", "KeyError", "ValueError", "NameError"],
        "answer": 2,
    },
    {
        "question": "클래스 메서드의 첫 번째 매개변수로 관례상 쓰이며, 인스턴스 자기 자신을 가리키는 것은?",
        "choices": ["this", "self", "cls", "instance"],
        "answer": 2,
    },
    {
        "question": "json.dump()로 한글을 저장할 때 \\uXXXX 형태가 아닌 원래 글자로 저장하려면?",
        "choices": ["indent=4", "sort_keys=True", "encoding='utf-8'", "ensure_ascii=False"],
        "answer": 4,
    },
    {
        "question": "with 문으로 파일을 열었을 때의 장점은?",
        "choices": ["파일이 자동으로 닫힌다", "파일이 압축된다", "읽기 속도가 빨라진다", "파일이 백업된다"],
        "answer": 1,
    },
    {
        "question": "반복 횟수가 정해져 있지 않고, 조건이 참인 동안 계속 반복할 때 적합한 것은?",
        "choices": ["for", "while", "if", "try"],
        "answer": 2,
    },
]


def create_default_quizzes():
    """기본 퀴즈 데이터를 Quiz 객체 리스트로 변환한다."""
    return [Quiz.from_dict(data) for data in DEFAULT_QUIZ_DATA]   

def read_int(prompt, low, high):
    """low~high 범위의 정수를 입력받는다. 올바른 값이 나올 때까지 반복."""
    while True:
        raw = input(prompt).strip()

        if not raw:                       # 빈 입력 (그냥 Enter)
            print(f"⚠️ 입력이 비어 있습니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue

        try:
            value = int(raw)              # 숫자 변환 실패
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue

        if not low <= value <= high:      # 허용 범위 밖
            print(f"⚠️ 범위를 벗어났습니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue

        return value


def read_text(prompt):
    """비어 있지 않은 문자열을 입력받는다."""
    while True:
        raw = input(prompt).strip()
        if raw:
            return raw
        print("⚠️ 내용을 입력해 주세요.")

def play_quiz(quizzes):
    """퀴즈를 순서대로 출제하고 맞힌 개수를 반환한다."""
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
        return None

    total = len(quizzes)
    score = 0

    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

    for number, quiz in enumerate(quizzes, start=1):
        print("\n" + "-" * 40)
        quiz.show(number)
        user_answer = read_int("\n정답 입력: ", 1, 4)

        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번 ({quiz.answer_text()}) 입니다.")

    print("\n" + "=" * 40)
    print(f"🏆 결과: {total}문제 중 {score}문제 정답!")
    print("=" * 40)

    return score

def main():
    quizzes = create_default_quizzes()
    while True:
        print(MENU)
        choice = read_int("선택: ", 1, 5)

        if choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            print("\n[퀴즈 추가] 준비 중입니다.")
        elif choice == 3:
            print("\n[퀴즈 목록] 준비 중입니다.")
        elif choice == 4:
            print("\n[점수 확인] 준비 중입니다.")
        elif choice == 5:
            print("\n👋 게임을 종료합니다.")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램을 종료합니다.")