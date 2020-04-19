from enum import Enum
import struct


class MessageType(Enum):
    Bearings = 0
    Status = 1



class BearingsMessageSerializer:

    def serialize_data(self, bearings: list):
        bearings_count = len(bearings)
        format = 'ii' + 'f'*bearings_count
        serialized_data = struct.pack(format, MessageType.Bearings.value, bearings_count, *bearings)

        return serialized_data



class MessageDeserializer:

    def __init__(self, data):
        self.data = data

    def __get_mesage_type(self):
        data = self.data[:4]
        result = struct.unpack('i', data)[0]
        return MessageType(result)
        
    def deserialize_data(self):

        message_type = self.__get_mesage_type()
        if message_type == MessageType.Bearings:
            data = self.data[4:8]
            bearings_count = struct.unpack('i', data)[0]
            data = self.data[8:]
            bearings = struct.unpack('f'*bearings_count, data)
            return message_type, bearings

            

        elif self.message_type == MessageType.Status:
            pass