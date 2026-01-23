import "./globals.css";

export const metadata = {
  title: "Admin | Guess the Number",
  description: "Manage panel of the Telegram bot",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header>
          <div className="w-full h-32 font-bold bg-primary flex justify-center hover:shadow-2xl items-center text-center">
            <p className="text-7xl text-text-on-primary">Угадай число</p>
          </div>
        </header>
        {children}
      </body>
    </html>
  );
}
