import { h } from 'preact';
import { Router } from 'preact-router';

import Home from './pages/Home';
export function App() {
  return (
    <ThemeProvider>
      <UserProvider>
        <div id="app" className="min-h-screen flex flex-col">
          <Header />
          <main className="overflow-y-auto overflow-x-hidden hide-scroll h-svh w-svw [perspective:1px] font-lato flex flex-col justify-between items-center">
            <div className='w-full'>
              <Router>
                <Home path="/" />
              </Router>
            </div>
            <Footer />
          </main>
        </div>
      </UserProvider>
    </ThemeProvider>
  );
}
