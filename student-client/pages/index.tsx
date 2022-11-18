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
    fetch("https://8fb6-129-110-242-176.ngrok.io/question?user=bh9000&question=" + question)
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

  const addMessage = (msg: string, containsMath: boolean) => {
    setMessages((messages) => [
      ...messages,
      {
        text: msg,
        fromUser: true,
        containsMath,
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
