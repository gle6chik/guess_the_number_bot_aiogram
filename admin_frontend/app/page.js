import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Админ-панель Telegram бота
        </h1>
        <p className="text-gray-600 mb-16">
          Панель управления находится в разработке
        </p>
        <div className="space-x-20">
          <Link
            href="/login"
            className="bg-blue-600 text-white px-20 py-7 rounded-4xl font-bold text-6xl hover:bg-blue-300 hover:text-gray-700 transition"
          >
            Войти
          </Link>
        </div>
      </div>
    </div>
  );
}