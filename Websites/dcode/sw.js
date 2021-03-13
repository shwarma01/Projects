self.addEventListener("install", (e) => {
  // When you change anything here remeber to skip waiting for the service worker
  e.waitUntil(
    caches.open("static").then((cache) => {
      return cache.addAll(["./index.html", "./src/master.css", "./images/logo192.png"]);
    })
  );
});

self.addEventListener("fetch", (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});
