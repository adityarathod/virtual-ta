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
  const addMessage = (msg: string, containsMath: boolean) => {
    setMessages([
      ...messages,
      {
        text: msg,
        fromUser: true,
        containsMath,
      },
      {
        text: "I'm not connected to a backend yet so I'm useless :(",
        fromUser: false,
      },
    ]);
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
