import Link from "next/link";
import Image from "next/image";

export default function Navbar() {
  return (
    <nav className="w-full flex flex-row items-center py-4 px-8 border-b-[2px]">
      <Link href="/">
        <Image
          src="/logo.svg"
          alt="Virtual TA Logo"
          width={150}
          height={50}
          className="cursor-pointer"
        />
      </Link>
      <div className="flex-1"></div>
      <div className="ml-6 text-xl font-semibold py-2 px-4 rounded-full bg-purple-600 text-white">
        CS 4349 (A. Chida)
      </div>
    </nav>
  );
}
