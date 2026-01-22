import "./globals.css";

export const metadata = {
  title: "Admin | Guess the Number",
  description: "Manage panel of the Telegram bot",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={"antialiased"}>
        <header>
          <div className="w-full h-32 font-bold bg-blue-600 flex justify-center items-center text-center">
            <p className="text-7xl text-white">Угадай число</p>
          </div>
        </header>
        {children}
      </body>
    </html>
  );
}
