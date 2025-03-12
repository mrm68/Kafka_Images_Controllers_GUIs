```markdown
# Apache Kafka Deployment Templates with Docker Compose

![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

A curated collection of production-ready Docker Compose templates for Apache Kafka deployments, featuring multiple configuration approaches and management interfaces.

## Key Features

- **Multi-Configuration Support**: 
  - Bitnami & Confluent platform implementations
  - KRaft mode and traditional ZooKeeper configurations
  - Isolated port assignments for parallel deployments

- **Integrated Management Interfaces**:
  - AKHQ (GUI for Kafka cluster management)
  - Kouncil (Web-based administration tool)
  - Provectus Kafka-UI (Monitoring and administration interface)

- **Production-Grade Configuration**:
  - Persistent volume configuration
  - Automated restart policies
  - Environment variable management
  - Security protocol mappings

## Getting Started

### Prerequisites
- Docker Engine 20.10+
- Docker Compose 2.0+
- 4GB RAM minimum allocation

### Quick Deployment
```bash
# Clone repository
git clone https://github.com/yourusername/kafka-deployment-templates.git
cd kafka-deployment-templates

# Set up environment
cp .env.example .env

# Start Bitnami/KRaft configuration
docker-compose -f BK_Bitnami_Kraft.yml up -d
```

Access management interfaces:
- **AKHQ**: http://localhost:8081
- **Kouncil**: http://localhost:8082
- **Provectus Kafka-UI**: http://localhost:8083

## Configuration Overview

### Deployment Architectures
| Configuration File                  | Components                          | Port Range |
|-------------------------------------|-------------------------------------|------------|
| `BK_Bitnami_Kraft.yml`              | Bitnami Kafka (KRaft) + Management | 8081-8083  |
| `BZ_Bitnami_Zookeeper.yml`          | Bitnami + ZooKeeper                | 8085-8087  |
| `CK_Confluentinc_Kraft.yml`         | Confluent Kafka (KRaft)            | 8089-8091  |
| `CZ_Confluentinc_Zookeeper.yml`     | Confluent + ZooKeeper              | 8093-8095  |

### Environment Management
The `.env` file provides centralized port configuration and environment variables management:
```env
# Bitnami KRaft Configuration
bk_broker_port_number=9093
bk_akhq_port_number=8081
bk_kouncil_port_number=8082
bk_provectus_port_number=8083
```

## Use Cases

### Development & Testing
- Rapid prototyping of event-driven architectures
- Performance comparison between KRaft and ZooKeeper modes
- Safe experimentation with different Kafka distributions

### Production Patterns
- Containerized deployment strategies
- Horizontal scaling demonstrations
- Disaster recovery configurations

### Learning Environment
- Kafka cluster management practice
- Consumer/producer pattern implementation
- Topic configuration experimentation

## Frequently Asked Questions

**Q: How do I avoid port conflicts between configurations?**  
A: Each configuration uses isolated port ranges defined in `.env` for conflict-free parallel operation

**Q: What's the difference between management UIs?**  
A: Each interface offers unique monitoring capabilities - AKHQ focuses on cluster health, Kouncil on message inspection, and Kafka-UI on visual management

**Q: How to persist data between deployments?**  
A: Mounted volumes in `./kafka/data` ensure data persistence across container restarts

## Contributing

This project welcomes contributions following our [contribution guidelines](CONTRIBUTING.md). Particularly valuable are:
- Additional configuration scenarios
- Security hardening implementations
- Performance optimization suggestions

## License

MIT License - See [LICENSE](LICENSE) for details
