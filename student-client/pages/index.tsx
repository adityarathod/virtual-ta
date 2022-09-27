import { useState } from "react";
import Head from "next/head";
import MessageBox from "../components/message-box";
import Navbar from "../components/navbar";

import type Message from "../types/message";
import MessageView from "../components/message-view";

const initialMessages: Message[] = [
  {
    text: "Hi there, I'm your virtual TA. How can I be of assistance?",
    fromUser: false,
  },
];

export default function Home() {
  const [messages, setMessages] = useState<Message[]>(initialMessages);

  const getAnswer = (question: string) => {
    fetch("http://127.0.0.1:5000/question?user=sunny&question=" + question)
      .then((res) => res.text())
      .then((response) => {
        setMessages((messages) => [
          ...messages,
          {
            text: response,
            fromUser: false,
          },
        ]);
        console.log(messages);
      });
  };

  const addMessage = (msg: string) => {
    setMessages((messages) => [
      ...messages,
      {
        text: msg,
        fromUser: true,
      },
    ]);
    getAnswer(msg);
  };
  return (
    <div className="flex w-screen h-screen flex-col">
      <Head>
        <title>Virtual TA</title>
      </Head>

      <Navbar />
      <MessageView messages={messages} />
      <MessageBox onSend={addMessage} />
    </div>
  );
}
