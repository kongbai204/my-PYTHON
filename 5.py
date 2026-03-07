import requests
import datetime
import os

# 世界气象组织（WMO）天气解释代码映射字典
WEATHER_CODES = {
    0: "晴朗",
    1: "少云",
    2: "局部多云",
    3: "阴天",
    45: "有雾",
    48: "有沉积霜雾",
    51: "毛毛雨: 细微",
    53: "毛毛雨: 中等",
    55: "毛毛雨: 密集",
    56: "冻毛毛雨: 细微",
    57: "冻毛毛雨: 密集",
    61: "下雨: 微弱",
    63: "下雨: 中等",
    65: "下雨: 强降水",
    66: "冻雨: 微弱",
    67: "冻雨: 强降水",
    71: "降雪: 微弱",
    73: "降雪: 中等",
    75: "降雪: 强降雪",
    77: "雪粒",
    80: "阵雨: 微弱",
    81: "阵雨: 中等",
    82: "阵雨: 强烈",
    85: "阵雪: 微弱",
    86: "阵雪: 强烈",
    95: "雷雨: 轻微或中等",
    96: "雷雨: 伴有轻微冰雹",
    99: "雷雨: 伴有强烈冰雹",
}

def get_city_coordinates(city_name):
    """调用 geocoding API 通过城市名字获取经纬度"""
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=zh"
    try:
        response = requests.get(geocode_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("results"):
            location = data["results"][0]
            return location.get("latitude"), location.get("longitude"), location.get("name", city_name)
    except Exception as e:
        print(f"获取城市坐标异常: {e}")
    return None, None, city_name

def generate_weather_report(city_name):
    """获取天气信息并生成中文报告"""
    # 1. 获取城市的经纬度
    lat, lon, official_name = get_city_coordinates(city_name)
    if lat is None or lon is None:
        return f"无法找到城市 '{city_name}' 的位置信息，请检查输入或网络状况。", False

    # 2. 获取实时天气数据 (使用 Open-Meteo API，无需密钥)
    weather_url = (f"https://api.open-meteo.com/v1/forecast"
                   f"?latitude={lat}&longitude={lon}"
                   f"&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m"
                   f"&timezone=auto")
    try:
        response = requests.get(weather_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        current = data.get("current", {})
        temp = current.get("temperature_2m", "N/A")
        feels_like = current.get("apparent_temperature", "N/A")
        humidity = current.get("relative_humidity_2m", "N/A")
        weather_code = current.get("weather_code", -1)
        wind_speed = current.get("wind_speed_10m", "N/A")
        
        # 将天气代号翻译成中文
        weather_desc = WEATHER_CODES.get(weather_code, f"未知天气 (代码: {weather_code})")
        
        # 3. 构造中文气象报告
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = f"===== 【{official_name}】天气报告 =====\n"
        report += f"查询时间: {now}\n"
        report += f"天气状况: {weather_desc}\n"
        report += f"当前温度: {temp}°C (体感温度: {feels_like}°C)\n"
        report += f"空气湿度: {humidity}%\n"
        report += f"当前风速: {wind_speed} km/h\n"
        report +=  "================================="
        
        return report, True
        
    except Exception as e:
        return f"获取【{official_name}】天气信息失败: {e}", False

def save_report_to_file(city_name, report_text):
    """将报告保存到当前的 txt 文件中"""
    filename = f"{city_name}_天气报告.txt"
    try:
        # 考虑到跨平台，使用 utf-8 编码写入文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"\n✅ 报告已自动保存到文件 -> {os.path.abspath(filename)}")
    except Exception as e:
        print(f"\n❌ 保存文件时发生错误: {e}")

def main():
    print("🌤️ 欢迎使用城市天气一键查询工具 🌤️")
    print("说明: 本工具基于免费公开接口 Open-Meteo 获取数据。")
    print("-" * 50)
    
    city_input = input("请输入你要查询的城市 (例如: 北京, Shanghai, 纽约): ").strip()
    
    if not city_input:
        print("⚠️ 城市名称不能为空！")
        return

    print(f"\n正在联网查询 {city_input} 的天气...")
    report, success = generate_weather_report(city_input)
    
    # 打印输出报告内容
    print("\n" + report)
    
    # 如果查询成功，则生成文件保存
    if success:
        save_report_to_file(city_input, report)

if __name__ == "__main__":
    main()
