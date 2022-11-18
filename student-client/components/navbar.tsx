import Link from "next/link";
import Image from "next/image";

export default function Navbar() {
  return (
    <nav className="w-full flex flex-row items-center py-1 px-8 border-b-[2px]">
      <Link href="/">
        <a>
          <Image
            src="/logo.svg"
            alt="Virtual TA Logo"
            width={100}
            height={50}
            className="cursor-pointer"
          />
        </a>
      </Link>
      <div className="flex-1"></div>
      <div className="ml-6 text-sm font-semibold py-1 px-3 rounded-full bg-purple-600 text-white">
        CS 4349 (A. Chida)
      </div>
    </nav>
  );
}
