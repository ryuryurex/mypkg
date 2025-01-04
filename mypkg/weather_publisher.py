import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
from datetime import datetime

class WeatherPublisher(Node):
    def __init__(self):
        super().__init__('weather_publisher')
        self.publisher_ = self.create_publisher(String, 'weather_info', 10)
        self.timer = self.create_timer(10.0, self.publish_weather_info)

    def publish_weather_info(self):
        # 千葉県習志野市の緯度と経度
        latitude = 35.6694
        longitude = 140.0167
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&temperature_unit=celsius&windspeed_unit=kmh&precipitation_unit=mm&timezone=Asia/Tokyo"

        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            current_weather = weather_data.get('current_weather', {})

            temperature = current_weather.get('temperature', 'N/A')
            wind_speed = current_weather.get('windspeed', 'N/A')
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            msg = String()
            msg.data = f"{temperature},{wind_speed},{timestamp}"
            self.publisher_.publish(msg)
        else:
            self.get_logger().warn(f"天気データの取得に失敗しました。HTTPステータスコード: {response.status_code}")

def main(args=None):
    rclpy.init(args=args)
    weather_publisher = WeatherPublisher()
    rclpy.spin(weather_publisher)
    weather_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

