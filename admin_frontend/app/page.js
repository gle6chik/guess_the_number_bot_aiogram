import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen flex justify-center bg-background">
      <div className="text-center mt-60">
        <h1 className="text-4xl font-bold text-text-primary mb-4">
          Админ-панель Telegram бота
        </h1>
        <p className="text-text-tertiary mb-16">
          Панель управления находится в разработке
        </p>
        <div>
          <Link
            href="/login"
            className="bg-primary text-text-on-primary px-20 py-4 rounded-4xl font-bold text-6xl hover:shadow-2xl hover:bg-hover hover:text-text transition duration-150"
          >
            Войти
          </Link>
        </div>
      </div>
    </div>
  );
}