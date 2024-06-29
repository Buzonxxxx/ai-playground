from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner

load_dotenv()

@tool
def check_inventory(flower_type: str) -> int:
    """
    查詢特定種類花的庫存數量。
    參數:
    - flower_type: 花的種類
    返回:
    - 庫存數量 (暫時返回一個固定的數字)
    """
    # 實際應用中這裡應該是資料庫查詢或其他形式的庫存檢查
    return 100  # 假設每種花都有100個單位

@tool
def calculate_price(base_price: float, markup: float) -> float:
    """
    根據基礎價格和加價百分比計算最終價格。
    參數:
    - base_price: 基礎價格
    - markup: 加價百分比
    返回:
    - 最終價格
    """
    return base_price * (1 + markup)

@tool
def schedule_delivery(order_id: int, delivery_date: str):
    """
    安排訂單的配送。
    參數:
    - order_id: 訂單編號
    - delivery_date: 配送日期
    返回:
    - 配送狀態或確認信息
    """
    # 在實際應用中這裡應該是對接配送系統的過程
    return f"訂單 {order_id} 已安排在 {delivery_date} 配送"

tools = [check_inventory, calculate_price]

model = ChatOpenAI(temperature=0)

planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.invoke("查查玫瑰的庫存然後给出出貨方案！")
