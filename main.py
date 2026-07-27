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