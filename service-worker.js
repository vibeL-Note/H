const CACHE_NAME = "game-calendar-v1";
const urlsToCache = [
  "/",
  "/index.html",
  "/manifest.json",
  "/data/events.json"
];

// 安装缓存
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
      .then(() => self.skipWaiting())
  );
});

// 激活缓存
self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keyList => {
      return Promise.all(keyList.map(key => {
        if (key !== CACHE_NAME) return caches.delete(key);
      }));
    }).then(() => self.clients.claim())
  );
});

// 缓存优先策略
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) return response;
        return fetch(event.request).then(res => {
          return caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, res.clone());
            return res;
          });
        });
      })
  );
});