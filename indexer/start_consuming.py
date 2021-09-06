from application.service import SaveBlogApplicationService
from di import DIManager
from port.adapter.messaging.rabbitmq import RabbitMQBlogSavedListener

di_manager = DIManager()

if __name__ == "__main__":
    RabbitMQBlogSavedListener(di_manager.get(SaveBlogApplicationService))
