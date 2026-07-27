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


def main():
    while True:
        print(MENU)
        choice = read_int("선택: ", 1, 5)

        if choice == 1:
            print("\n[퀴즈 풀기] 준비 중입니다.")
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