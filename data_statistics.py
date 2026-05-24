"""
论辩对话数据统计脚本
"""
import json

def analyze_debates_data(file_path):
    """
    分析论辩对话数据，统计其基本信息。
    :param file_path: 论辩对话数据文件路径
    """
    total = 0
    winner_a = 0
    winner_b = 0
    winner_null = 0
    rounds_lengths = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # 跳过空行
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                print(f"警告：无法解析的行 - {line[:50]}...")
                continue

            total += 1

            # 统计winner
            winner = data.get('winner')
            if winner == 'A':
                winner_a += 1
            elif winner == 'B':
                winner_b += 1
            else:
                winner_null += 1

            # 统计rounds长度
            rounds = data.get('rounds', [])
            rounds_lengths.append(len(rounds))

    if total == 0:
        print("文件中没有有效数据。")
        return

    # 计算比例
    pct_a = winner_a / total * 100
    pct_b = winner_b / total * 100
    pct_null = winner_null / total * 100
    pct_persuasive = (winner_a + winner_b) / total * 100
    pct_deadlocked = winner_null / total * 100

    # rounds长度统计
    max_rounds = max(rounds_lengths)
    min_rounds = min(rounds_lengths)
    avg_rounds = sum(rounds_lengths) / len(rounds_lengths)

    # 输出结果
    print("=" * 50)
    print("对话数据统计结果")
    print("=" * 50)
    print(f"总数据量：{total}")
    print("\n【胜方分布】")
    print(f"  A胜：{winner_a}条 ({pct_a:.2f}%)")
    print(f"  B胜：{winner_b}条 ({pct_b:.2f}%)")
    print(f"  null：{winner_null}条 ({pct_null:.2f}%)")
    print("\n【对话类型】")
    print(f"  说服型：{winner_a + winner_b}条 ({pct_persuasive:.2f}%)")
    print(f"  僵持型：{winner_null}条 ({pct_deadlocked:.2f}%)")
    print("\n【对话轮次长度】")
    print(f"  最大值：{max_rounds}轮")
    print(f"  最小值：{min_rounds}轮")
    print(f"  平均值：{avg_rounds:.2f}轮")
    print("=" * 50)

if __name__ == "__main__":
    file_path = "debates_data.jsonl"
    analyze_debates_data(file_path)