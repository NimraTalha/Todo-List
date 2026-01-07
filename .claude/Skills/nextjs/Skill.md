# Next.js Development

## Overview
This skill covers Next.js development best practices, patterns, and techniques. Next.js is a React framework that enables functionality such as server-side rendering, static site generation, and API routes.

## When to Use
Use this skill when:
- Building React applications with server-side rendering
- Creating static sites or hybrid applications
- Implementing API routes within your React application
- Optimizing performance and SEO
- Setting up routing and navigation
- Handling data fetching strategies

## Project Structure

### Standard Next.js Structure
```
my-nextjs-app/
├── node_modules/
├── pages/
│   ├── api/
│   │   └── hello.js
│   ├── _app.js
│   ├── _document.js
│   ├── index.js
│   └── [slug].js
├── public/
├── styles/
├── components/
├── package.json
└── next.config.js
```

### Modern App Router Structure (Next.js 13+)
```
my-nextjs-app/
├── app/
│   ├── layout.js
│   ├── page.js
│   ├── about/
│   │   └── page.js
│   ├── api/
│   │   └── route.js
│   └── globals.css
├── components/
├── public/
└── next.config.js
```

## Routing and Navigation

### Pages Router
```javascript
// pages/index.js
import Link from 'next/link';

export default function HomePage() {
  return (
    <div>
      <h1>Home Page</h1>
      <Link href="/about">
        <a>About Page</a>
      </Link>
    </div>
  );
}

// Dynamic routes: pages/users/[id].js
export default function UserPage({ user }) {
  return <div>User: {user.name}</div>;
}

export async function getStaticProps({ params }) {
  const user = await fetchUser(params.id);
  return {
    props: { user },
  };
}
```

### App Router (Next.js 13+)
```javascript
// app/page.js
import Link from 'next/link';

export default function HomePage() {
  return (
    <div>
      <h1>Home Page</h1>
      <Link href="/about">About Page</Link>
    </div>
  );
}

// Dynamic routes: app/users/[id]/page.js
export default async function UserPage({ params }) {
  const user = await fetchUser(params.id);

  return <div>User: {user.name}</div>;
}
```

## Data Fetching Strategies

### Server-Side Rendering (SSR)
```javascript
// pages/ssr-example.js
export async function getServerSideProps(context) {
  const data = await fetchData();

  return {
    props: { data }, // Will be passed to the page component
  };
}

export default function SSRPage({ data }) {
  return <div>{JSON.stringify(data)}</div>;
}
```

### Static Site Generation (SSG)
```javascript
// pages/ssg-example.js
export async function getStaticProps(context) {
  const data = await fetchData();

  return {
    props: { data },
    revalidate: 3600, // Rebuild page after 1 hour
  };
}

export default function SSGPage({ data }) {
  return <div>{JSON.stringify(data)}</div>;
}
```

### Incremental Static Regeneration (ISR)
```javascript
// pages/isr-example.js
export async function getStaticProps(context) {
  const data = await fetchData();

  return {
    props: { data },
    revalidate: 30, // Revalidate after 30 seconds
  };
}
```

### Client-Side Data Fetching
```javascript
// components/client-data.js
import { useState, useEffect } from 'react';

export default function ClientSideData() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('/api/data');
      const result = await response.json();
      setData(result);
      setLoading(false);
    }

    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (!data) return <div>No data</div>;

  return <div>{JSON.stringify(data)}</div>;
}
```

## API Routes

### Basic API Route
```javascript
// pages/api/hello.js
export default function handler(req, res) {
  res.status(200).json({ message: 'Hello World' });
}
```

### Advanced API Route with Database
```javascript
// pages/api/users.js
import dbConnect from '../../lib/dbConnect';
import User from '../../models/User';

export default async function handler(req, res) {
  const { method } = req;

  await dbConnect();

  switch (method) {
    case 'GET':
      try {
        const users = await User.find({});
        res.status(200).json({ success: true, data: users });
      } catch (error) {
        res.status(400).json({ success: false });
      }
      break;
    case 'POST':
      try {
        const user = await User.create(req.body);
        res.status(201).json({ success: true, data: user });
      } catch (error) {
        res.status(400).json({ success: false });
      }
      break;
    default:
      res.status(400).json({ success: false });
      break;
  }
}
```

## Performance Optimization

### Image Optimization
```javascript
import Image from 'next/image';

export default function OptimizedImage() {
  return (
    <Image
      src="/profile.jpg"
      alt="Profile"
      width={300}
      height={300}
      priority // For above-the-fold images
    />
  );
}
```

### Dynamic Imports
```javascript
import { useState } from 'react';

export default function DynamicImportExample() {
  const [showChart, setShowChart] = useState(false);
  const [Chart, setChart] = useState(null);

  const loadChart = async () => {
    const chartModule = await import('../components/Chart');
    setChart(chartModule.default);
  };

  return (
    <div>
      <button onClick={() => {
        setShowChart(true);
        loadChart();
      }}>
        Load Chart
      </button>
      {showChart && Chart && <Chart />}
    </div>
  );
}
```

### Preloading Pages
```javascript
import { useRouter } from 'next/router';
import Link from 'next/link';

export default function PreloadExample() {
  const router = useRouter();

  return (
    <div>
      <Link
        href="/dashboard"
        onMouseEnter={() => router.prefetch('/dashboard')}
      >
        Dashboard
      </Link>
    </div>
  );
}
```

## Environment Variables
```javascript
// .env.local
NEXT_PUBLIC_SITE_URL=https://example.com
DATABASE_URL=mongodb://localhost/myapp
```

```javascript
// pages/config.js
export default function ConfigPage() {
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL;
  const dbUrl = process.env.DATABASE_URL; // Only available server-side

  return (
    <div>
      <p>Site URL: {siteUrl}</p>
      <p>DB URL: {dbUrl ? 'Configured' : 'Not configured'}</p>
    </div>
  );
}
```

## Error Handling

### Custom Error Page
```javascript
// pages/_error.js
import Error from 'next/error';

const MyError = ({ statusCode, hasGetInitialPropsRun, err }) => {
  if (!hasGetInitialPropsRun && err) {
    // Log the error to an error reporting service
    console.error(err);
  }

  return <Error statusCode={statusCode} />;
};

MyError.getInitialProps = async ({ res, err }) => {
  const errorInitialProps = await Error.getInitialProps({ res, err });

  // Workaround for https://github.com/vercel/next.js/issues/8592
  const hasGetInitialPropsRun = true;

  return { ...errorInitialProps, hasGetInitialPropsRun };
};

export default MyError;
```

## Best Practices

1. **Use the App Router when possible** (Next.js 13+) for better performance and developer experience
2. **Implement proper error boundaries** to handle React errors gracefully
3. **Optimize images** using Next.js Image component
4. **Use dynamic imports** for code splitting
5. **Leverage Next.js built-in CSS support** and CSS-in-JS solutions
6. **Implement proper SEO** with next/head component
7. **Use environment variables** for configuration
8. **Implement proper loading states** for better UX
9. **Use TypeScript** for better type safety
10. **Follow Next.js file-based routing conventions**

## Deployment
- Use Vercel for optimal Next.js deployment (created by the Next.js team)
- Ensure proper environment variable configuration
- Set up custom domains and SSL certificates
- Configure build and deployment scripts
- Monitor performance and errors