import React, { useEffect, useState } from 'react';
import { Phone, Zap, TrendingDown, BarChart3, Sparkles } from 'lucide-react';

export default function SivoBenefits() {
  const [hoveredCard, setHoveredCard] = useState(null);
  const [autoPaused, setAutoPaused] = useState(false);

  const benefits = [
    {
      id: 1,
      icon: Phone,
      title: 'Atención 24/7',
      subtitle: 'Siempre disponible para tus clientes',
      description: 'Tu SIVO nunca duerme. Atiende llamadas, chats y consultas en cualquier momento del día, todos los días del año.',
      bgColor: 'bg-blue-50',
      iconBg: 'bg-white',
      iconColor: 'text-blue-600',
      gradientColor: 'from-blue-500 to-cyan-500'
    },
    {
      id: 2,
      icon: Zap,
      title: 'Automatización Inteligente',
      subtitle: 'Libera tiempo valioso',
      description: 'Automatiza tareas repetitivas como reservas, consultas frecuentes y seguimiento de pedidos. Tu equipo se enfoca en lo importante.',
      bgColor: 'bg-purple-50',
      iconBg: 'bg-white',
      iconColor: 'text-purple-600',
      gradientColor: 'from-purple-500 to-pink-500'
    },
    {
      id: 3,
      icon: TrendingDown,
      title: 'Reduce Costos',
      subtitle: 'Hasta 70% de ahorro',
      description: 'Elimina costos de contratación, capacitación y turnos nocturnos. Un SIVO reemplaza múltiples agentes a una fracción del costo.',
      bgColor: 'bg-green-50',
      iconBg: 'bg-white',
      iconColor: 'text-green-600',
      gradientColor: 'from-green-500 to-emerald-500'
    },
    {
      id: 4,
      icon: BarChart3,
      title: 'Escalabilidad Instantánea',
      subtitle: 'Crece sin límites',
      description: 'Atiende 1 o 1000 clientes simultáneamente sin contratar más personal. Escala tu negocio sin preocupaciones.',
      bgColor: 'bg-orange-50',
      iconBg: 'bg-white',
      iconColor: 'text-orange-600',
      gradientColor: 'from-orange-500 to-red-500'
    }
  ];

  // Auto-hover (ciclo automático) para activar el efecto sin mouse
  useEffect(() => {
    if (autoPaused) return;

    const ids = benefits.map((b) => b.id);
    if (!ids.length) return;

    let i = 0;
    // Arranca activando la primera tarjeta
    setHoveredCard(ids[0]);

    const interval = setInterval(() => {
      i = (i + 1) % ids.length;
      setHoveredCard(ids[i]);
    }, 1600);

    return () => clearInterval(interval);
  }, [autoPaused]);


  return (
    <div className="bg-white py-16 px-4">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-3">
            Beneficios de tener un SIVO
          </h2>
          <p className="text-lg text-gray-600">
            Transforma tu negocio con inteligencia artificial.{' '}
            <span className="font-semibold">Estos son solo algunos de los beneficios.</span>
          </p>
        </div>

        {/* Benefits Horizontal Scroll */}
        <div className="relative">
          <div className="flex gap-6 overflow-x-auto pb-4 px-4 snap-x snap-mandatory scrollbar-hide">
            {benefits.map((benefit) => {
              const Icon = benefit.icon;
              const isHovered = hoveredCard === benefit.id;

              return (
                <div
                  key={benefit.id}
                  className="relative flex-shrink-0 w-80 h-72 rounded-2xl overflow-hidden cursor-pointer snap-center"
                  onMouseEnter={() => { setAutoPaused(true); setHoveredCard(benefit.id); }}
                  onMouseLeave={() => { setHoveredCard(null); setAutoPaused(false); }}
                  onTouchStart={() => { setAutoPaused(true); setHoveredCard(benefit.id); }}
                  onTouchEnd={() => { setHoveredCard(null); setAutoPaused(false); }}
                >
                  {/* Front Card - Simple Design */}
                  <div
                    className={`absolute inset-0 ${benefit.bgColor} p-8 text-center transition-transform duration-500 ease-out ${
                      isHovered ? '-translate-x-full' : 'translate-x-0'
                    }`}
                  >
                    {/* Icon */}
                    <div className="flex justify-center mb-6">
                      <div className={`${benefit.iconBg} w-16 h-16 rounded-full shadow-md flex items-center justify-center`}>
                        <Icon className={`w-8 h-8 ${benefit.iconColor}`} strokeWidth={2.5} />
                      </div>
                    </div>

                    {/* Content */}
                    <h3 className="text-xl font-bold text-gray-900 mb-2">
                      {benefit.title}
                    </h3>
                    <p className="text-gray-600 text-sm mb-6">
                      {benefit.subtitle}
                    </p>

                    {/* Hover indicator */}
                    <div className="absolute bottom-6 left-0 right-0">
                      <span className="text-gray-500 text-sm inline-flex items-center gap-1">
                        Desliza para ver más
                        <svg 
                          className="w-4 h-4" 
                          fill="none" 
                          stroke="currentColor" 
                          viewBox="0 0 24 24"
                        >
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                        </svg>
                      </span>
                    </div>
                  </div>

                  {/* Back Card - Slides in from right */}
                  <div
                    className={`absolute inset-0 bg-gradient-to-br ${benefit.gradientColor} p-8 flex flex-col justify-center text-white transition-transform duration-500 ease-out ${
                      isHovered ? 'translate-x-0' : 'translate-x-full'
                    }`}
                  >
                    <div className="mb-4">
                      <Icon className="w-12 h-12 mb-3 opacity-90" />
                      <h3 className="text-2xl font-bold mb-2">
                        {benefit.title}
                      </h3>
                    </div>
                    <p className="text-white/95 leading-relaxed">
                      {benefit.description}
                    </p>
                    
                    {/* Decorative element */}
                    <div className="absolute top-6 right-6 opacity-20">
                      <Sparkles className="w-8 h-8" />
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
          
          {/* Scroll Indicators */}
          <div className="flex justify-center gap-2 mt-6">
            {benefits.map((benefit) => (
              <div 
                key={benefit.id}
                className="w-2 h-2 rounded-full bg-gray-300"
              />
            ))}
          </div>
        </div>

        {/* CSS for hiding scrollbar */}
        <style jsx>{`
          .scrollbar-hide::-webkit-scrollbar {
            display: none;
          }
          .scrollbar-hide {
            -ms-overflow-style: none;
            scrollbar-width: none;
          }
        `}</style>
      </div>
    </div>
  );
}
