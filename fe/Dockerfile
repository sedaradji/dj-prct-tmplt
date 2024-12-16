# Use an official Node.js runtime as a parent image
FROM node:18-alpine

ARG USE_S3
ARG S3_BUCKET


ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
ENV AWS_DEFAULT_REGION=
ENV EXEC_ENV=
ENV S3_BUCKET=${S3_BUCKET}
ENV USE_S3=${USE_S3}

# Set the working directory in the container
WORKDIR .

# Copy package.json and package-lock.json (if available)
COPY ./package.json ./package-lock.json* ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

# Install AWS CLI
RUN apk add aws-cli

# Change the CMD to upload to S3
CMD ["sh","-c","aws s3 sync dist s3://${S3_BUCKET} --delete"]