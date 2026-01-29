import Link from "next/link";

export default function InfoLayout({ children }) {
    return (
        <div>
            <main>
                {children}
            </main>
            <footer>
                <div className="w-full bg-gray-400 mt-36 px-10 py-4">
                    <div className="flex flex-col gap-2">
                        <div className="flex flex-row items-center">
                            <img src="/icons8-telegram-50.png" alt="Telegram icon" className="w-6 h-6 mr-2" />
                            <Link href="https://t.me/guess_this_number_bot">
                                <p className="text-white text-base">Перейти в бота</p>
                            </Link>
                        </div>
                        <div className="flex flex-row items-center">
                            <img src="/icons8-github-50.png" alt="GitHub icon" className="w-6 h-6 mr-2" />
                            <Link href="https://github.com/gle6chik/guess_the_number_bot_aiogram">
                                <p className="text-white text-base">Репозиторий GitHub</p>
                            </Link>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
}