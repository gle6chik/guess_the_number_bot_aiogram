import Link from "next/link";

export default function InfoLayout({ children }) {
    return (
        <div>
            <main>
                {children}
            </main>
            <footer>
                <div className="w-full h-64 bg-gray-500 mt-36 p-10 flex items-center justify-center">
                    <div className="flex flex-col gap-3">
                        <div className="flex flex-row gap-3 items-center justify-center">
                            <img src="/icons8-telegram-app-50.png" alt="Telegram icon" />
                            <Link href="https://t.me/guess_this_number_bot">
                                <p className="text-white text-2xl">Перейти в бота</p>
                            </Link>
                        </div>
                        <div className="flex flex-row gap-3 items-center">
                            <img src="/icons8-github-50.png" alt="GitHub icon" />
                            <Link href="https://github.com/gle6chik/guess_the_number_bot_aiogram">
                                <p className="text-white text-2xl">Репозиторий GitHub</p>
                            </Link>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
}