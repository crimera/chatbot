from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Message():
    name: str
    text: str

    def render(self):
        return f"{self.name}: {self.text}"

@dataclass(frozen=True)
class Conversation():
    messages: List[Message]
    
    def render(self): 
        return "\n".join(
            [message.render() for message in self.messages]
        )

@dataclass(frozen=True)
class Prompt():
    header: Message
    name: str
    example_conversations: List[Conversation]
    conversation: Conversation

    def render(self):
        example_conversations = "\n\n".join(
            [conversation.render() for conversation in self.example_conversations]
        )
        return "\n".join(
            [self.header.render()]
            + ["Example conversation:"]
            + [example_conversations.strip()]
            + ["Current conversation:"]
            + [self.conversation.render()]
            + [f"{self.name}: "]
        )

@dataclass(frozen=True)
class Config():
    instructions: str
    example_conversations: List[Conversation]

def test():
    conversation = Conversation(messages=[Message("steven", "hello"), Message("kotoko", "hi")])
    print(
        Prompt(
            header=Message("system", "you are a yandere"),
            example_conversations=[conversation, conversation],
            conversation=conversation
        ).render()
    )