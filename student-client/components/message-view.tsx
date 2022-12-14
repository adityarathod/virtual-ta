import classNames from "classnames";
import { useEffect, useRef } from "react";
import Message from "../types/message";
import Latex from "react-latex";

interface MessageViewProps {
  messages: Message[];
}

export default function MessageView({ messages }: MessageViewProps) {
  const sectionRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!sectionRef.current) return;
    sectionRef.current.scrollTop = sectionRef.current.scrollHeight;
  }, [messages]);
  return (
    <section className="flex-1 px-8 py-4 overflow-scroll" ref={sectionRef}>
      {messages.map((msg, idx) => (
        <ChatMessage message={msg} key={idx} />
      ))}
    </section>
  );
}

interface ChatMessageProps {
  message: Message;
}

function ChatMessage({ message }: ChatMessageProps) {
  const { text, fromUser } = message;

  let textClasses = classNames(
    "py-3 px-4",
    "my-2",
    "text-md",
    "w-full md:w-[60%] xl:w-[45%]",
    fromUser ? "bg-userHighlight" : "bg-gray-300",
    fromUser ? "text-white" : "text-black",
    "rounded-t-xl",
    fromUser ? "rounded-bl-xl" : "rounded-br-xl"
  );

  return (
    <div
      className={classNames(
        "flex",
        "flex-row",
        "w-full",
        fromUser && "justify-end"
      )}
    >
      {fromUser ?
        <div className={textClasses}>
          {message.containsMath ? <Latex>{text}</Latex> : <span>{text}</span>}
        </div>
        :
        <div className={textClasses} dangerouslySetInnerHTML={{ __html: text }}></div>
      }
    </div>
  );
}
