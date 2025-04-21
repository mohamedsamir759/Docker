
FROM node:18-alpine
WORKDIR /node.js
COPY package*.json ./
RUN npm install --production
ENV NODE_ENV=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]

